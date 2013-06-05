#!/usr/bin/ruby
frequencies = Hash.new(0)
File.open("queries.txt") do |file|
#File.open("mini") do |file|
#	file.each {|line| my_match = /query.*?,/.match(line); frequencies[my_match.to_s] += 1 }
	file.each {|line| my_match = /query=(.+?,)/.match(line); 
			if !my_match.nil? 
				frequencies[my_match[1]] += 1
			 end 
		  }
end
frequencies = frequencies.sort{|a, b| b[1] <=> a[1]}
frequencies = frequencies.select{|k, v| v > 0}
#frequencies = Hash[frequencies.to_a.reverse]
frequencies.each {|a, b| puts "#{a} => #{b}" }
