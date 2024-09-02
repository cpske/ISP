## Django Review Questions


10.  Your application receives the request GET /polls/4/ but there is no poll with id=4.  What should the KU Polls application return?  Describe how you would handle this, not just the response code. There is more than one acceptable answer to this.

- "Redirect the user to the index page".

   Good but you must also display an error message on the page so the user knows why he was redirected there.

- "Return a 404 Error Page and Redirect the browser to the index page"

   You can't do both. Either return a 404 status code or redirect to another page and include an error message on that page.
