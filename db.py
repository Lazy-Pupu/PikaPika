from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    created = db.Column(db.DateTime)


class MonitorFolders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=True)
    created = db.Column(db.DateTime)


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    icon = db.Column(db.String(80), unique=True, nullable=True)
    is_generated = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime)


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    icon = db.Column(db.String(80), unique=True, nullable=True)
    created = db.Column(db.DateTime)


class Tagging(db.Model):
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'),
                       primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'),
                         primary_key=True)
