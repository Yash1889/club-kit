# RSVP form with a short link

Print a short link (for example `yoursite.org/rsvp`) on flyers instead of a long form URL. When the next event
comes, point the short link at the new form and every printed QR code keeps working.

## 1. Make the form

Use whatever form tool your school provides (Microsoft Forms works with a school account). Ask only what you'll use:

1. Name
2. Email
3. Which best describes you (student, alum, attorney or other)
4. Class year, if a student
5. Organization
6. In person or online
7. Dietary or accessibility needs

Set it so anyone with the link can respond if you're inviting people outside the school.

## 2. Make the short link

On a site hosted with Cloudflare Pages or Netlify, add a redirect rule to the `_redirects` file:

```
/rsvp   https://forms.example.com/your-form-id   302
/rsvp/  https://forms.example.com/your-form-id   302
```

Use `302` (temporary) so browsers don't cache it and you can repoint it later.

## 3. Make the QR code

```sh
python3 qr/make_qr.py https://yoursite.org/rsvp rsvp-qr.png
```

Test it with a phone before printing.
