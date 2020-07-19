import os, shutil
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.template.loader import render_to_string

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()


def main():
    print("Let's build.")
    deploy_dir = settings.DEPLOY_DIR

    print("Removing existing deploy dir, if any...")
    shutil.rmtree(deploy_dir, ignore_errors=True)

    print("Copying contents of static/ into deploy...")
    shutil.copytree(settings.STATIC_DIR, deploy_dir)

    print("Rendering pages...")
    pages = settings.PAGES_TO_RENDER
    for page in pages:
        print(f"Rendering {page}")
        rendered = render_to_string(f"{page}.html", {
            **settings.CONTEXT, "page": page
        })
        page_path = os.path.join(deploy_dir, f"{page}.html")
        fout = open(page_path, 'w')
        fout.write(rendered)
        fout.close()

    print("Done")


if __name__ == "__main__":
    main()
