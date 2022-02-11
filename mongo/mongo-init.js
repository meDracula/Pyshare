db.createUser({
	user: "albin",
	pwd: "password",
	roles: [
		{
		role: "readWrite",
		db: "pysharedb",
		},
		]
	}
);

db.createUser({
	user: "abshir",
	pwd: "password",
	roles: [
		{
		role: "readWrite",
		db: "pysharedb",
		},
		]
	}
);

db.createUser({
	user: "elvir",
	pwd: "password",
	roles: [
		{
		role: "readWrite",
		db: "pysharedb",
		},
		]
	}
);

db.createUser({
	user: "mohammad",
	pwd: "password",
	roles: [
		{
		role: "readWrite",
		db: "pysharedb",
		},
		]
	}
);

db.users.createIndex({ username: 1 }, { unique: true } );
db.users.createIndex({ email: 1 }, { unique: true } );
db.posts.createIndex({ title: 1 }, { unique: true } );
db.posts.createIndex({ title_hash: 1 }, { unique: true } );
db.posts.createIndex({ title: "text" });
db.posts.createIndex({ created: -1 });
