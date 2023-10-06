#!/usr/bin/env ruby

input = ARGV[0]

pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

matches = input.scan(pattern).map { |match| match.join(",") }

puts matches.join("\n")
