import unittest
from unittest.mock import patch
from chrome import chrome_bp
from flask import Flask

class TestChromeAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(chrome_bp, url_prefix='/chrome')
        self.client = self.app.test_client()

    def test_chrome_basic_endpoint(self):
        """기본 Chrome 엔드포인트 테스트"""
        response = self.client.post('/chrome/', 
                                  json={'keyword': 'test'},
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Chrome 호출 성공')

    def test_open_url_missing_url(self):
        """URL이 없는 경우 테스트"""
        response = self.client.post('/chrome/open',
                                  json={},
                                  content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'URL이 필요합니다')

    @patch('webbrowser.open')
    def test_open_url_success(self, mock_open):
        """URL 열기 성공 테스트"""
        test_url = 'https://www.example.com'
        response = self.client.post('/chrome/open',
                                  json={'url': test_url},
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'URL이 성공적으로 열렸습니다')
        mock_open.assert_called_once_with(test_url)

    @patch('webbrowser.open')
    def test_open_url_failure(self, mock_open):
        """URL 열기 실패 테스트"""
        mock_open.side_effect = Exception('브라우저 오류')
        response = self.client.post('/chrome/open',
                                  json={'url': 'https://www.example.com'},
                                  content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertIn('URL을 여는 중 오류 발생', response.json['error'])

if __name__ == '__main__':
    unittest.main() 