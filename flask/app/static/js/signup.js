function verify_password() {
	password1 = document.getElementById('password1').innerHTML;
	password2 = document.getElementById('password2').innerHTML;
	if (password1 === password2) {
		document.getElementById('submit').disabled = false;
	}
	else {
		document.getElementById('submit').disabled = true;
	}
}
