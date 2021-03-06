/**
 * @param {string[]} words
 * @return {number}
 */
var minimumLengthEncoding = function(words) {
    words.sort((a,b) => b.length - a.length);
    let ansStr = words[0] + '#';
    for(let i = 1; i < words.length; i++) {
        const temp = ansStr.split('#');
        let filled = false;
        for(const word of temp) {
            if(word.length > words[i].length) {
                const ind = word.length - words[i].length;
                if(word.slice(ind,ind + words[i].length) === words[i]) {
                    filled = true;
                    break
                }
            } else if(word === words[i]) {
                filled = true;
                break
            } else {
                continue;
            }
        }
        if(!filled) {
            ansStr += words[i] + '#';
        }
    }
    return ansStr.length;
};