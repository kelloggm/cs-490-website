bundle exec jekyll build
rm -rf ../martinjkellogg.com/teaching/cs485-sp26
cp -r _site ../martinjkellogg.com/teaching/cs485-sp26
cd ../martinjkellogg.com/
git add teaching/cs485-sp26
git commit -m "update cs485"
git push
