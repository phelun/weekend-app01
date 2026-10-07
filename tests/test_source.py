from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class App01SourceTests(unittest.TestCase):
    def test_page_has_expected_heading(self):
        page = (ROOT / "src/index.html").read_text(encoding="utf-8")
        self.assertIn("Welcome to App01 Local", page)

    def test_nginx_routes_internal_services_by_kubernetes_dns(self):
        config = (ROOT / "src/default.conf").read_text(encoding="utf-8")
        self.assertIn("app02-service.app02-weekend-com.svc.cluster.local", config)
        self.assertIn("app03-service.app03-weekend-com.svc.cluster.local", config)
        self.assertIn("location = /healthz", config)


if __name__ == "__main__":
    unittest.main()
