from app import db

class Link(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	short_link = db.Column(db.String(6), index=True, unique=True)
	destination = db.Column(db.String(180), index=True, unique=True)

	def __repr__(self):
		return 'Link: %r %r' % (self.short_link, self.destination)