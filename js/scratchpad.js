tries      = 0
challenge  = document.custom.generateSignature()
signature  = document.custom.generateSignature()

document.custom.addSpan()
counterTag = document.getElementById(document.custom.spanCount)



while(signature[1] != challenge[1] || 
      signature[5] != challenge[5] ||
      signature[4] != challenge[4] 
    ) {
    tries = tries  + 1
    signature = document.custom.generateSignature() 
    triesSpan = document.getElementById(document.custom.spanCount)
    triesSpan.innerText = tries
}
console.log('signature: ' + signature)
console.log('challenge: ' + challenge)
console.log(tries)