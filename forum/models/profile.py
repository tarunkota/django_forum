from django.db import models    
from django.contrib.auth.models import User
from .badges import Badge
from django.utils import timezone
from .. import utils
from django.dispatch import receiver
from django.db.models.signals import post_save
import random

class Profile(models.Model):
    """Profile of the user.
    """
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    username = models.CharField(max_length=128,unique=True,default="")
    firstname = models.CharField(max_length=128,blank=True)
    lastname = models.CharField(max_length=128,blank=True)

    dp = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True,default=0)
    badges = models.ManyToManyField(Badge, blank=True)

    contact_list = models.ManyToManyField(User, related_name='contacters', blank=True)
    pending_list = models.ManyToManyField(User, related_name='my_pending_requests', blank=True)
    member_since = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        """override save
        """
        if(self.username==""):
            self.username = utils.generateRandomUsername()
            # check if unique
            while(Profile.objects.filter(username=self.username).exists()):
                self.username = utils.generateRandomUsername()
                
        super(Profile, self).save(*args,**kwargs)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

class Avatar(models.Model):
    """
    """
    profile =  models.OneToOneField(Profile, null=True, related_name='avatar', on_delete=models.CASCADE)
    background = models.CharField(max_length=64,default="Circle")
    topType = models.CharField(max_length=64,default="")
    accessoriesType = models.CharField(max_length=64,default="")
    hairColor = models.CharField(max_length=64,default="")
    facialHairType = models.CharField(max_length=64,default="")
    facialHairColor = models.CharField(max_length=64,default="")
    clotheType = models.CharField(max_length=64,default="")
    clotheColor = models.CharField(max_length=64,default="")
    graphicType = models.CharField(max_length=64,default="")
    eyeType = models.CharField(max_length=64,default="")
    eyebrowType = models.CharField(max_length=64,default="")
    mouthType = models.CharField(max_length=64,default="")
    skinColor = models.CharField(max_length=64,default="")

    def __str__(self):
        return str(self.profile)

    def save(self, *args, **kwargs):
        """override save
        """
        topType=["NoHair","Eyepatch","Hat","Hijab","Turban","WinterHat1","WinterHat2","WinterHat3","WinterHat4","LongHairBigHair","LongHairBob","LongHairBun","LongHairCurly","LongHairCurvy","LongHairDreads","LongHairFrida","LongHairFro","LongHairFroBand","LongHairNotTooLong","LongHairShavedSides","LongHairMiaWallace","LongHairStraight","LongHairStraight2","LongHairStraightStrand","ShortHairDreads01","ShortHairDreads02","ShortHairFrizzle","ShortHairShaggyMullet","ShortHairShortCurly","ShortHairShortFlat","ShortHairShortRound","ShortHairShortWaved","ShortHairSides","ShortHairTheCaesar","ShortHairTheCaesarSidePart"]
        accessoriesType=["Blank","Kurt","Prescription01","Prescription02","Round","Sunglasses","Wayfarers"]  
        hairColor=["Auburn","Black","Blonde","BlondeGolden","Brown","BrownDark","PastelPink","Blue","Platinum","Red","SilverGray"]
        facialHairType=["Blank","BeardMedium","BeardLight","BeardMajestic","MoustacheFancy","MoustacheMagnum"]          
        facialHairColor=["Auburn","Black","Blonde","BlondeGolden","Brown","BrownDark","Platinum","Red"]
        clotheType=["BlazerShirt","BlazerSweater","CollarSweater","GraphicShirt","Hoodie","Overall","ShirtCrewNeck","ShirtScoopNeck","ShirtVNeck"]
        clotheColor=["Black","Blue01","Blue02","Blue03","Gray01","Gray02","Heather","PastelBlue","PastelGreen","PastelOrange","PastelRed","PastelYellow","Pink","Red","White"]
        graphicType=["Bat","Cumbia","Deer","Diamond","Hola","Pizza","Resist","Selena","Bear","SkullOutline","Skull"]
        eyeType = ["Close","Cry","Default","Dizzy","EyeRoll","Happy","Hearts","Side","Squint","Surprised","Wink","WinkWacky"]
        eyebrowType=["Angry","AngryNatural","Default","DefaultNatural","FlatNatural","RaisedExcited","RaisedExcitedNatural","SadConcerned","SadConcernedNatural","UnibrowNatural","UpDown","UpDownNatural"]
        mouthType=["Concerned","Default","Disbelief","Eating","Grimace","Sad","ScreamOpen","Serious","Smile","Tongue","Twinkle","Vomit"]
        skinColor=["Tanned","Yellow","Pale","Light","Brown","DarkBrown","Black"]

        if(self.topType ==""):
            self.topType = random.choice(topType)
        if(self.accessoriesType ==""):
            self.accessoriesType = random.choice(accessoriesType)
        if(self.hairColor ==""):
            self.hairColor = random.choice(hairColor)
        if(self.facialHairType ==""):
            self.facialHairType = random.choice(facialHairType)
        if(self.facialHairColor ==""):
            self.facialHairColor = random.choice(facialHairColor)
        if(self.clotheType ==""):
            self.clotheType = random.choice(clotheType)
        if(self.clotheColor ==""):
            self.clotheColor = random.choice(clotheColor)
        if(self.graphicType ==""):
            self.graphicType = random.choice(graphicType)
        if(self.eyeType  ==""):
            self.eyeType  = random.choice(eyeType )
        if(self.eyebrowType ==""):
            self.eyebrowType = random.choice(eyebrowType)
        if(self.mouthType ==""):
            self.mouthType = random.choice(mouthType)
        if(self.skinColor ==""):
            self.skinColor = random.choice(skinColor)

        super(Avatar, self).save(*args, **kwargs)

