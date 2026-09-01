#!/bin/bash
# END-OF-SEMESTER ARCHIVAL SNAPSHOT --- this is no longer the deployment process.
#
# The live site is deployed automatically by .github/workflows/pages.yml on every
# push to the semester branch, to https://kelloggm.github.io/cs-490-website/.
# While the semester is running, martinjkellogg.com/teaching/cs490-au26/ holds
# redirect stubs pointing at that live site.
#
# Historically the site was built here and copied into the personal website
# (originally hosted on an NJIT server, later on GitHub Pages), which is why the
# old URLs are nested under /teaching/.
#
# Run this ONCE after the semester ends, before the next semester's branch takes
# over the live URL. It overwrites the redirect stubs with a frozen copy of the
# final site, so that the old teaching/ URL becomes a permanent archive --- the
# same way every previous semester is archived.
set -euo pipefail

SEMESTER=cs490-au26
BASEURL="/martinjkellogg.com/teaching/${SEMESTER}"

# The archive is served from the personal site, so it has to be rebuilt with the
# personal site's baseurl rather than the one in _config.yml.
bundle exec jekyll build --baseurl "$BASEURL"

rm -rf "../martinjkellogg.com/teaching/${SEMESTER}"
cp -r _site "../martinjkellogg.com/teaching/${SEMESTER}"
cd ../martinjkellogg.com/
git add "teaching/${SEMESTER}"
git commit -m "archive ${SEMESTER} course website"
git push
