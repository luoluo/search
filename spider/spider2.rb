require 'rubygems'
require 'open-uri'

url_hash = {}

open('lf2013.github.io').each do |i|
	`wget i.html`
end	
