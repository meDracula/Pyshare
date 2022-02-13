function upvote(input) {
	const params = { title_hash: input.value, vote: 1 };

	fetch("http://127.0.0.1/ajax/post_vote", {
		method: 'POST',
		headers: { 'Content-type': 'application/json' },
		body: JSON.stringify(params)
		})
		.catch(error => alert(error));
	input.checked = true;
}

function downvote(input) {
	const params = { title_hash: input.value, vote: -1 };

	fetch("http://127.0.0.1/ajax/post_vote", {
		method: 'POST',
		headers: { 'Content-type': 'application/json' },
		body: JSON.stringify(params)
		})
		.catch(error => alert(error));
	input.checked = true;
}
