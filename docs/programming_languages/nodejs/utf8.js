const fs = require('fs');

let result = fs.readFileSync('../utf8.txt', {encoding: 'utf-8'});
let delim = result.indexOf("\r\n") >= 0 ? "\r\n" : "\n";

result = result.split(delim);
var content = ""
for (let i=0; i<result.length; i++){
    line = result[i];
    if (line){
        let grapheme = [...new Intl.Segmenter().segment(line)];
        let joinedGSegments = grapheme.map(seg => {
            return seg.segment;
        })
        content += "String: " + line
        content += "\nString type: " + typeof(line);
        content += "\nList: " + line.split('');
        content += "\nSeventh Character: " + line[6]
        content += "\nGrapheme(s)" + joinedGSegments.join(', ');
        content += "\nLength: " + line.length + "\nList Length: " + line.split('').length + "\nGrapheme(s) length: " + grapheme.length + "\n\n";
    }
}
console.log(content);
fs.writeFileSync('./output.txt', content);

