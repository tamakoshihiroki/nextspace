function set_width( enable ) {
  col = document.getElementsByName( 'column' ).item( 0 );
  row = document.getElementsByName( 'row' ).item( 0 );
  col.disabled = enable;
  row.disabled = enable;
  return false;
}
