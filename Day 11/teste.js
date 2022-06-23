/*
Crie uma função de nome contaLetras que recebe uma palavra como parâmetro.
Essa função deve contar (print) quantas das letras dessa palavra são vogais e quantas são consoantes.
Essa função deve também trazer em uma lista (print) quais são as vogais dessa palavra e em outra lista quais são as consoantes.
*/

palavra = "mesa"

function contaLetras(palavra) {
    let vogaisPalavra = [];
    let contaVogais = 0;
    let consoantesPalavra = []
    let contaConsoantes = 0;

    let vogais = ["a", "e", "i", "o", "u"]

    for (let index = 0; index < palavra.length; index++) {
        if (vogais.includes(palavra[index])) {
            contaVogais += 1;
            vogaisPalavra.push(palavra[index]);
        } else {
            contaConsoantes += 1;
            consoantesPalavra.push(palavra[index])
        }
    }
    console.log(`As vogais são: ${vogaisPalavra}, somando ${contaVogais} vogais ao todo.`)
    console.log(`As consoantes são: ${consoantesPalavra}, somando ${contaConsoantes} vogais ao todo.`)

}

contaLetras(palavra)
