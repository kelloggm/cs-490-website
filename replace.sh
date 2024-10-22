bundle exec jekyll build
rm -rf ../martinjkellogg.com/teaching/cs485-sp25
cp -r _site ../martinjkellogg.com/teaching/cs485-sp25
cd ../martinjkellogg.com/
git add teaching/cs485-sp25
git commit -m "update cs485"
git push
