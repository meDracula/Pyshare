function switch_username_email(){
	if (document.getElementById('username_or_email').checked) {
		document.getElementById('user_identifier').innerHTML = "Email";
	}
	else{
		document.getElementById('user_identifier').innerHTML = "Username";
	}
}
