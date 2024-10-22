bundle exec jekyll build
rm -rf ../martinjkellogg.com/teaching/cs490-au24
cp -r _site ../martinjkellogg.com/teaching/cs490-au24
cd ../martinjkellogg.com/
git add teaching/cs490-au24
git commit -m "update cs490"
git push
