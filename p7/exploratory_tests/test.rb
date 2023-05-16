data, _ = IO.select([$stdin])
loop do
  print $stdin.read_nonblock(1)
rescue SystemCallError
  break
end
