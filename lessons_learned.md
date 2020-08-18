# Lessons Learned

## Dash

1. Passing params into Dash from Flask

    In this app, users input a postcode on the first page (ie. in `flask`), which is validated through the `postcodes.io` api. To pass the first half of this (the incode) into Dash I did the following:

   * Saved `incode` to the flask session
   * Registered a Dash app at `/dashapp1/`
   * Appended the incode to the url for the Dash app on `postcode_info.html`: `{{ url_for('/dashapp1/') + '#' + session.incode }}`
   * Added `Location` component to the Dash layout to access the url: `dcc.Location(id="incode", refresh=True)`
   * Specify that the callback for this app is on the url refreshing, and access just the hash element of the url: `[Input("incode", "hash")]`

    Important that the tag (incode) matches between the Location and Input classes. Refresh needs to be set in Location so that the callback is triggered when the page is launched.

## Flask

