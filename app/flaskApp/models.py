from flaskAPI import db


class CoStarData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10000), unique=True, nullable=False)
    summary = db.Column(db.String(10000), unique=True, nullable=False)
    body = db.Column(db.String(10000), unique=True, nullable=False)
    hits = db.Column(db.Integer, nullable=True) 
    authorID = db.Column(db.Integer, nullable=True)
    createdDate = db.Column(db.String(100), unique=True, nullable=False)
    Country_USA = db.Column(db.Integer, nullable=True)
    Country_CAN = db.Column(db.Integer, nullable=True)
    Country_GBR = db.Column(db.Integer, nullable=True)
    Tag_None = db.Column(db.Integer, nullable=True)
    Tag_National = db.Column(db.Integer, nullable=True)
    Tag_Office	= db.Column(db.Integer, nullable=True)
    Tag_Industrial	= db.Column(db.Integer, nullable=True)
    Tag_Retail= db.Column(db.Integer, nullable=True)
    Tag_People = db.Column(db.Integer, nullable=True)
    Tag_Investment = db.Column(db.Integer, nullable=True)
    Tag_Analytics = db.Column(db.Integer, nullable=True)
    Tag_Development = db.Column(db.Integer, nullable=True)
    Tag_Finance = db.Column(db.Integer, nullable=True)
    Tag_Events = db.Column(db.Integer, nullable=True)
    Tag_Multifamily = db.Column(db.Integer, nullable=True)
    Tag_Hospitality = db.Column(db.Integer, nullable=True)
    Tag_Company = db.Column(db.Integer, nullable=True)
    Tag_Healthcare = db.Column(db.Integer, nullable=True)
    Tag_Legal = db.Column(db.Integer, nullable=True)
    Tag_Land = db.Column(db.Integer, nullable=True)
    Tag_Lease = db.Column(db.Integer, nullable=True)
    Tag_Sale = db.Column(db.Integer, nullable=True)
    Tag_MixedUse = db.Column(db.Integer, nullable=True)
    Tag_SpecialPurpose = db.Column(db.Integer, nullable=True)
    Tag_PublicSector = db.Column(db.Integer, nullable=True)
    Tag_CompaniesPeople = db.Column(db.Integer, nullable=True)
    Tag_CoStarGreenReport = db.Column(db.Integer, nullable=True)
    word_count = db.Column(db.Integer, nullable=True)
    #Corpus 


