
// Recuperer l'argument
// print process.argv
keys = []
process.argv.forEach(function (val, index, array) {
  // console.log(index + ': ' + val);
  keys.push(val);
});

key = keys[2];

console.log(key);

console.log(encoded(key));

function encoded(b)
{
  //var b=$(this).data('content'),

  // b is the key we need to decode

  var d="",
  f,e,h,c,g,a=0;

  for(b=b.replace(/[^A-Za-z0-9\+\/\=]/g,""); a<b.length;)
  {
    f="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".indexOf(b.charAt(a++));
    e="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".indexOf(b.charAt(a++));
    c="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".indexOf(b.charAt(a++));
    g="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".indexOf(b.charAt(a++));

    f=f<<2|e>>4;e=(e&15)<<4|c>>2;h=(c&3)<<6|g;d+=String.fromCharCode(f);

    if(c!=64)d+=String.fromCharCode(e);
    if(g!=64)d+=String.fromCharCode(h)
  }

  b="";

    for(c=c1=c2=a=0;a<d.length;)
    {
      c=d.charCodeAt(a);
      if(c<128)
      {
        b+=String.fromCharCode(c);
        a++
      }
      else if(c>191&&c<224)
      {
        c2=d.charCodeAt(a+1);
        b+=String.fromCharCode((c&31)<<6|c2&63);
        a+=2
      }
      else
      {
        c2=d.charCodeAt(a+1);
        c3=d.charCodeAt(a+2);
        b+=String.fromCharCode((c&15)<<12|(c2&63)<<6|c3&63);
        a+=3
      }
    }
    // $(this).replaceWith(b)
    return b
};
