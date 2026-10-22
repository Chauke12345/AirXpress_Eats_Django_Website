# AirXpress Eats Django Public Website Template

A starter Django app for the public-facing marketing website. It does **not** implement website food ordering. Customers are directed to the existing app: https://web-production-81fc2.up.railway.app/

## Included
- Responsive home page and navigation
- Partner-shop directory and individual profile pages
- Driver information and partner enquiry pages
- Contact page with your supplied emails and telephone number
- Django admin to add, edit, feature, deactivate and reorder shops
- Shop logos uploaded through admin; active shops appear automatically

## Important
This is a starter template, not yet integrated into your current AirXpress Eats repository. Merge it into a backup/copy first. Do not replace existing `orders`, payment, driver, settings or database files.

## Setup
1. Back up your existing project or create a Git branch.
2. Copy the `publicsite` folder into the folder containing `manage.py`.
3. Add `publicsite` to `INSTALLED_APPS` in `settings.py`.
4. Add `AIRXPRESS_APP_URL = "https://web-production-81fc2.up.railway.app/"` to settings.
5. Configure media uploads if not already configured: `MEDIA_URL = "/media/"` and `MEDIA_ROOT = BASE_DIR / "media"`.
6. In the project's root `urls.py`, add `path("", include("publicsite.urls"))` only if the root URL is available. If an existing app already uses `/`, resolve the route conflict first.
7. Install image support: `pip install Pillow`.
8. Run `python manage.py makemigrations publicsite`
9. Run `python manage.py migrate`
10. Create an admin user if needed: `python manage.py createsuperuser`.
11. Run `python manage.py runserver` and visit `/admin/`.
12. Add these confirmed shops in admin, upload the correct logo files and enter only verified details:
    - Mozake & Sons Catering Services
    - Naledi's
    - The Love of Alex
    - Porangi World
    - Vele Ns Catering
    - Munchie Fellas

## Adding shops later
Use Django admin to add another Partner Shop, upload its logo, fill in its profile and set `is_active`. It appears automatically in the public directory. Feature a shop by ticking `app_featured`.

## Production checklist
- Configure persistent media storage for production; do not assume uploaded files on local Railway disk persist.
- Set `AIRXPRESS_APP_URL` in production settings/environment.
- Review route conflicts, privacy policy, terms and consent wording.
- Test in a staging copy before deploying.
