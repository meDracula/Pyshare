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

db.status.insertOne({ status: 'confirmed' });

