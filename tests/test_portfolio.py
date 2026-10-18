"""Browser regressions for the static portfolio. No external app writes."""
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import unittest
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class PortfolioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT)))
        Thread(target=cls.server.serve_forever, daemon=True).start()
        cls.url = f'http://127.0.0.1:{cls.server.server_port}/'
        cls.pw = sync_playwright().start()
        options = {'headless': True}
        if os.getenv('BROWSER_CHANNEL'):
            options['channel'] = os.environ['BROWSER_CHANNEL']
        cls.browser = cls.pw.chromium.launch(**options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()
        cls.server.shutdown()
        cls.server.server_close()

    def setUp(self):
        self.page = self.browser.new_page(viewport={'width':1440, 'height':900})
        self.page.goto(self.url, wait_until='networkidle')
        self.page.evaluate('document.fonts.ready')

    def tearDown(self):
        self.page.close()

    def test_keyboard_skip_and_disclosures(self):
        page = self.page
        page.keyboard.press('Tab')
        self.assertEqual(page.locator(':focus').inner_text(), 'Skip to projects')
        self.assertGreaterEqual(page.locator(':focus').bounding_box()['y'], 0)
        page.keyboard.press('Enter')
        self.assertEqual(page.locator(':focus').get_attribute('id'), 'projects')
        page.keyboard.press('Tab')
        self.assertEqual(page.locator(':focus').inner_text(), 'Enter the Sportsbook')
        for summary in page.locator('summary').all():
            summary.focus()
            page.keyboard.press('Enter')
            self.assertTrue(summary.locator('..').evaluate('(el)=>el.open'))
            page.keyboard.press('Space')
            self.assertFalse(summary.locator('..').evaluate('(el)=>el.open'))
        self.assertEqual(page.locator('[tabindex="0"], .social').count(), 0)

    def test_real_links_activate_with_mouse_and_enter(self):
        page = self.page
        destinations = {
            'Enter the Sportsbook': 'https://sportsbook.coopergurrie.com/',
            'Try the public demo': 'https://sportsbook.coopergurrie.com/#/demo',
            'Open the NCAAB Model': 'https://cbb.coopergurrie.com/',
            'Explore historical winner performance': 'https://cbb.coopergurrie.com/#performance',
        }
        # Intercept destinations so this regression test stays offline and read-only.
        page.route('https://**/*', lambda route: route.fulfill(body='<title>Destination</title><p>Destination</p>', content_type='text/html'))
        for label, target in destinations.items():
            for action in ['mouse', 'keyboard']:
                page.goto(self.url)
                page.locator('article details').evaluate_all('(els)=>els.forEach(el=>el.open=true)')
                link = page.get_by_role('link', name=label, exact=True)
                if action == 'mouse':
                    link.click()
                else:
                    link.focus()
                    page.keyboard.press('Enter')
                page.wait_for_url(target)
                self.assertEqual(page.url, target)

    def test_narrow_layout_and_expanded_content(self):
        page = self.page
        page.emulate_media(reduced_motion='reduce')
        for width in [320,390,768,1440]:
            page.set_viewport_size({'width':width,'height':844})
            for expanded in [False,True]:
                page.locator('details').evaluate_all('(els,open)=>els.forEach(el=>el.open=open)', expanded)
                self.assertLessEqual(page.evaluate('document.documentElement.scrollWidth'), width)
                for heading in page.locator('h1,h2').all():
                    self.assertLessEqual(heading.evaluate('(el)=>el.scrollWidth'), heading.evaluate('(el)=>el.clientWidth'))
        page.set_viewport_size({'width':390,'height':844})
        page.locator('details').evaluate_all('(els)=>els.forEach(el=>el.open=false)')
        self.assertLess(page.locator('.projects').bounding_box()['y'], 320)
        self.assertLess(page.locator('#basketball').bounding_box()['y'], 844)

    def test_media_loads_and_metadata_agrees(self):
        page = self.page
        page.locator('article details').evaluate_all('(els)=>els.forEach(el=>el.open=true)')
        for img in page.locator('article img').all():
            img.scroll_into_view_if_needed()
            page.wait_for_function('(src)=>{const img=document.querySelector(`img[src="${src}"]`);return img.complete && img.naturalWidth>0}', arg=img.get_attribute('src'))
            self.assertEqual(img.evaluate('(el)=>el.naturalWidth'), 1280)
            self.assertTrue(img.get_attribute('alt'))
            self.assertEqual(img.get_attribute('width'), '1280')
            self.assertEqual(img.get_attribute('height'), '900')
        self.assertEqual(page.locator('meta[name="description"]').get_attribute('content'), page.locator('meta[property="og:description"]').get_attribute('content'))
        self.assertNotIn('Auto IG', page.content())
        for asset in ['assets/cooper-share.png','assets/cooper-favicon.svg','assets/sportsbook-demo.webp','assets/basketball-research.webp']:
            self.assertEqual(page.request.get(self.url + asset).status, 200)
        self.assertEqual(page.evaluate('''async url=>{const img=new Image();img.src=url;await img.decode();return [img.naturalWidth,img.naturalHeight]}''', self.url + 'assets/cooper-share.png'), [1200,630])

    def test_reduced_motion(self):
        page = self.page
        page.emulate_media(reduced_motion='reduce')
        panel = page.locator('.project').first
        panel.hover()
        self.assertEqual(panel.evaluate('(el)=>getComputedStyle(el).transform'), 'none')
        self.assertEqual(page.locator('.orbit-lines').evaluate('(el)=>getComputedStyle(el).animationName'), 'none')
        self.assertEqual(page.locator('.background').evaluate('(el)=>getComputedStyle(el).transform'), 'none')

    def test_contacts_are_real_keyboard_and_mouse_links(self):
        page = self.page
        page.route('https://www.linkedin.com/**', lambda route: route.fulfill(body='<title>LinkedIn destination</title>', content_type='text/html'))
        for action in ['mouse', 'keyboard']:
            page.goto(self.url)
            linkedin = page.get_by_role('link', name='Cooper Gurrie on LinkedIn', exact=True)
            if action == 'mouse':
                linkedin.click()
            else:
                linkedin.focus()
                page.keyboard.press('Enter')
            page.wait_for_url('https://www.linkedin.com/in/coopergurrie/')
            page.goto(self.url)
            email = page.get_by_role('link', name='Email Cooper Gurrie', exact=True)
            self.assertEqual(email.get_attribute('href'), 'mailto:cooper.gurrie@gmail.com')
            # Verify native activation without opening a mail client or sending mail.
            email.evaluate('''el=>el.addEventListener('click', e=>{e.preventDefault();el.dataset.activated='yes'})''')
            if action == 'mouse':
                email.click()
            else:
                email.focus()
                page.keyboard.press('Enter')
            self.assertEqual(email.get_attribute('data-activated'), 'yes')

    def test_text_spacing_does_not_clip_card_content(self):
        page = self.page
        page.add_style_tag(content='*{line-height:1.5!important;letter-spacing:.12em!important;word-spacing:.16em!important}p{margin-bottom:2em!important}')
        for width in [320,1440]:
            page.set_viewport_size({'width':width,'height':900})
            for expanded in [False,True]:
                page.locator('details').evaluate_all('(els,open)=>els.forEach(el=>el.open=open)', expanded)
                self.assertLessEqual(page.evaluate('document.documentElement.scrollWidth'), width)
                self.assertFalse(page.locator('.project').evaluate_all('(els)=>els.some(el=>el.scrollHeight>el.clientHeight+1)'))


if __name__ == '__main__':
    unittest.main()
