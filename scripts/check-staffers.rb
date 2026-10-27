#!/usr/bin/env ruby
# Fails if any _staffers/*.md file will not actually appear on the built site.
# Run after `bundle exec jekyll build`. A staffer can silently vanish when, e.g.,
# their `role:` is misspelled (staff.md filters on exact role names) or their
# front matter does not parse (also caught by `strict_front_matter` in _config.yml).
require 'yaml'
require 'cgi'

def page_text(path)
  abort "check-staffers: #{path} not found; build the site first" unless File.exist?(path)
  # Decode entities and straighten curly quotes so names like O'Brien match.
  CGI.unescapeHTML(File.read(path)).tr("‘’“”", %q(''""))
end

staff = page_text('_site/staff/index.html')
hours = page_text('_site/office-hours/index.html')
errors = []

Dir.glob('_staffers/*.md').sort.each do |file|
  m = File.read(file).match(/\A---\s*\n(.*?)\n---\s*$/m)
  next errors << "#{file}: no front matter block" unless m
  begin
    data = YAML.safe_load(m[1]) || {}
  rescue Psych::Exception => e
    next errors << "#{file}: invalid YAML front matter (#{e.message})"
  end
  name = data['name'].to_s.strip
  next errors << "#{file}: missing `name:`" if name.empty?
  unless staff.include?(name)
    errors << "#{file}: #{name} does not appear on the staff page " \
              "(role is #{data['role'].inspect}; staff.md shows only 'Instructor' and 'Teaching Assistant')"
  end
  if data['office_hours'].is_a?(Array) && !data['office_hours'].empty? && !hours.include?(name)
    errors << "#{file}: #{name} has office_hours but does not appear on the office-hours page"
  end
end

if errors.empty?
  puts "check-staffers: all #{Dir.glob('_staffers/*.md').size} staffers are displayed"
else
  warn errors.map { |e| "check-staffers: #{e}" }
  exit 1
end
