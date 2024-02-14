alert( null || 2 || undefined ); //2



alert( alert(1) || 2 || alert(3) );

// The answer: first 1, then 2.



alert( 1 && null && 2 );

// The answer: null


alert( alert(1) && alert(2) );

// The answer: 1, and then undefined.



alert( null || 2 && 3 || 4 );

// The answer: 3.


if (age >= 14 && age <= 90)



if (age < 14 || age > 90)




if (-1 || 0) alert( 'first' );
if (-1 && 0) alert( 'second' );
if (null || -1 && 1) alert( 'third' );

// The answer: the first and the third will execute.



let userName = prompt("Who's there?", '');

if (userName === 'Admin') {

  let pass = prompt('Password?', '');

  if (pass === 'TheMaster') {
    alert( 'Welcome!' );
  } else if (pass === '' || pass === null) {
    alert( 'Canceled' );
  } else {
    alert( 'Wrong password' );
  }

} else if (userName === '' || userName === null) {
  alert( 'Canceled' );
} else {
  alert( "I don't know you" );
}