# beproofreading.com

Site assets for beproofreading.com

Generate html files from Django templates, combine with static assets, upload to S3.

## How to use

* Make page modifications in `templates`.
* Make context variable modifications in `settings`.
* Run `make run` and browse `localhost:3000` to see updates.
* Set up named profile in AWS credentials file.
* Run `make deploy` to upload.

## How to reuse

* Pull this repo into the child repo.
* In `templates`, delete all but `base.html` and `index.html`.
* Delete unwanted assets In `static`.
* Minimize `index.html`.
* Edit `settings.py`:
  - Update EMAIL setting.
  - Set PAGES\_TO\_RENDER to `("index",)`.
* Start using.
