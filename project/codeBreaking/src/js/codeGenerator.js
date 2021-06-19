export class GermanCode{
    constructor(charList, codeAlphabet){
        this.charList = charList;
        this.codeAlphabet = codeAlphabet;
        this.codeBookSize = this.codeAlphabet.length;
        this.codeBook;
        this.updateCodeBook();
    }

    updateCodeBook(){
        this.codeBook = this.shuffle(this.charList);
    }

    shuffle(list){
        const listLen = list.length;
        for(let i=0; i<listLen; i++){
            const targetIndex = this.getRandomNum(listLen);
            const targetCh = list[targetIndex];
            list[targetIndex] = list[i]
            list[i] = targetCh;
        }
        return list
    }

    getRandomNum(max){
        return Math.floor(Math.random() * max);       
    }

    getCodeBookStr(){
        let codeBookStr = ""
        for(let i=0; i<this.codeBookSize; i++){
            for(let j=0; j<this.codeBookSize; j++){
                codeBookStr += this.codeBook[i * this.codeBookSize + j]
            }
            codeBookStr += "\n"
        }
        return codeBookStr;
    }

    makeCode(targetStr){
        let ciphertext = ""
        const targetLen = targetStr.length;
        for(let i=0; i<targetLen; i++){
            ciphertext += this.getEncryptedCh(targetStr[i]);
        }
        return ciphertext;
    }

    getEncryptedCh(ch){
        const i = this.getIndexOf(ch);
        const row = this.getRowInCodeBook(i);
        const col = this.getColInCodeBook(i);
        return this.codeAlphabet[row] + this.codeAlphabet[col];
    }

    getIndexOf(ch){
        return this.codeBook.indexOf(ch);
    }

    getRowInCodeBook(index){
        return Math.floor(index / this.codeBookSize);
    }

    getColInCodeBook(index){
        return index % this.codeBookSize;
    }

    breakCode(code){
        let decryptedCode = ""
        if(code.length % 2 !== 0){
            decryptedCode = "Wrong Code"
        } else{
            const charLen = parseInt(code.length / 2);
            for(let i=0; i<charLen; i++){
                decryptedCode += this.getDecryptedCh(code[i*2] + code[i*2 + 1]);
            }
        }
        return decryptedCode;
    }

    getDecryptedCh(ch){
        const rowInCodeBook = ch[0];
        const colInCodeBook = ch[1];
        const i = this.getIndexInCodeAlphabet(rowInCodeBook) * this.codeBookSize + this.getIndexInCodeAlphabet(colInCodeBook);
        return this.codeBook[i];
    }

    getIndexInCodeAlphabet(ch){
        return this.codeAlphabet.indexOf(ch);
    }
}


