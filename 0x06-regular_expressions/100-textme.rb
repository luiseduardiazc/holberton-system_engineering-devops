#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:|to:).\w+|(?<=flags:)[-:0-9]+/).join(',')
