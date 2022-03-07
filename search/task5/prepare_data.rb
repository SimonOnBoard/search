
def get_data_from_file(name)
  data = File.open("../task4_1/#{name}")
    .read.split("\n")
  
  splitted_data = data.map { |i| i.split(" ") }
  splitted_data.map do |i|
    [i[0], "0.#{i.last.split(".").last}"]
  end
end

def prepare_all_data
  files = Dir.entries("../task4_1")
    .select { |i| ![".", ".."].include?(i) }
    .map do |i|
      { i => Hash[get_data_from_file(i)] }
    end
  return files
end

def tokens
  @tokens ||= prepare_all_data.map { |i| i.values.map {|j| j.map {|k| k[0]}} }.flatten.uniq
end

f = File.new("./tokens", "w")
f.write(tokens.join("\n"))

data = nil

prepare_all_data.map do |elem|
  data ||= prepare_all_data
  file = File.new("./vectors/#{elem.keys.first}", 'w')
  tokens.each do |token|
    a = elem.values.first
    file.write("#{token} #{a[token] || 0}\n")
  end
end
