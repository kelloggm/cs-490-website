bundle exec jekyll build
rm -rf ../martinjkellogg.com/teaching/cs490-au26
cp -r _site ../martinjkellogg.com/teaching/cs490-au26
cd ../martinjkellogg.com/
git add teaching/cs490-au26
git commit -m "update cs490"
git push
