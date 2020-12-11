from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Enum
from blanco.database import Base

import enum


class UserSexEnum(enum.Enum):
    """
    Agender - 无性别。没有发育性别、或者没有感觉到自己有任何强烈性别归属的人。他们不见得认为自己没有性别，但可能觉得性别不是自己的核心特质。
Androgyne - 两性人（名词）。拥有混合特征或者两种特征都很强烈的人。更强调对内的自我认同。
Androgynous - 两性人（形容词）。和上面的基本同义，但更强调对外的表现。
Bigender - 双性人。自我性别认定可以在两种之间切换的人。两种性别未必是男和女，可以是这里提到的许多种其它非传统性别。
Cis - 顺性人。自我性别认定和出生时的生物性别相同的人。大部分人归于此类。
Cis Female - 顺性女。出生时生物性别是女性，自己也觉得自己是女性。
Cis Woman - 顺性女。和上面的基本同义，略微更强调性征。
Cis Male - 顺性男。出生时生物性别是男性，自己也觉得自己是男性。
Cis Man - 顺性男。参见上上条。
Cisgender - 顺性人。和Cis意思相同，一个全写一个简写。使用全写的人认为这样更显职业特色，使用简写的人认为这样更日常更亲切，没有其他区别。以下四条同此，不再赘述。
Cisgender Female - 顺性女。
Cisgender Male - 顺性男。
Cisgender Man - 顺性男。
Cisgender Woman - 顺性女。
Female to Male - 女变男。出生时被归属为女性，但是已经完成或正在进行向男性自我认同的转变的人。这样的转变可以是完全心理和社会上的，也可以伴随手术和激素疗法。这个标签可以是转变过程中的暂时标签；也可以是永久性的，表明这个人认为出生性别也是自己生命的一部分。
FTM - 女变男。和上一条意思相同，是它的首字母缩写。
Gender Fluid - 流性人。在不同时间经历性别认知改变的人。和Bigender（双性人）不同的是，双性人在两种明确的状态间切换，而流性人的变化是连续谱。事实上，几乎每个人的性别都有流动特质，比如一位女性周围都是其它女性时，她的女性特征和认同往往会更强烈；但大部分人不会自我认同为流性人。
Gender Nonconforming - 非常规性别。拒绝接受传统性别二元区分的人。事实上这里的56种性别里很多都不是二元区分——但是选择这一选项的人，强调的是自己的拒绝特征：我不属于传统二元，但我也不会去精确定位自己的位置。下面有好几个选项和它意思类似。
Gender Questioning - 性别存疑。对自己的性别归属不完全确定、还没有找到最适合自己的性别认同标签的人。
Gender Variant - 变体性别。和非常规性别类似。
Genderqueer - 酷儿性别。和非常规性别类似。“酷儿”（Queer）这个词本意是奇怪，但是最近几十年来已经成为非传统性别的代称词语之一，并衍生出了“酷儿理论”这个研究性别角色的文化理论。
Intersex - 间性人。由于染色体或发育异常而拥有男女双方性征的人。
Male to Female - 男变女。参见女变男。
MTF - 男变女。同上。
Neither - 男女皆非。参见非常规性别，但并不强调拒绝含义。通常是那些知道自己不属于传统二元男女、但是不熟悉相关术语的人。
Neutrois - 无性别。和agender类似。
Non-binary - 非二元。和非常规性别类似。
Other - 其他。和男女皆非类似。
Pangender - 泛性别。认为自己是各种性别特质的混合体，每样都有一点儿。
Trans - 跨性别。和顺性别相对，自我性别认定和出生时生物性别不同。注意，跨性别不是非常规性别，跨性别者还是会使用男女二元论，只不过他们的自我认同恰好和出生性别相反。跨性别者可能有、也可能没有经历过性别转换。
Trans Female - 跨性女。出生时是男性，但现在自我认同女性。
Trans Male - 跨性男。出生时是女性，但现在自我认同男性。
Trans Man - 跨性男。参见顺性的相关讨论。
Trans Person - 跨性人。不愿明确指出自己从哪跨到哪的人。
Trans Woman - 跨性女。参见顺性的相关讨论。
Trans* - 跨性别*。加一个星号用来表示更加广义的意思，包括跨性、变性、酷儿性别等等相关领域。下同。
Trans* Female - 跨性女*。
Trans* Male - 跨性男*。
Trans* Man - 跨性男*。
Trans* Person - 跨性人*。
Trans* Woman - 跨性女*。
Transfeminine - 跨性女（形容词）。参见Androgyne和Androgynous的区别。较之Transwoman，Transfeminine更强调对外的跨性表现。
Transgender - 跨性别。和Trans基本意思相同。参见Cis和cisgender的相关讨论。下同。
Transgender Female - 跨性女
Transgender Male - 跨性男。
Transgender Man - 跨性男。
Transgender Person - 跨性人。
Transgender Woman - 跨性女
Transmasculine - 跨性男（形容词）。参见跨性女（形容词）。
Transsexual - 变性别。不但自我认同性别与出生性别不同，还采取了医学措施、改变了自己的生理和解剖特征的人。
Transsexual Female - 变性女。
Transsexual Male - 变性男。
Transsexual Man - 变性男。
Transsexual Person - 变性人。
Transsexual Woman - 变性女。
Two-spirit - 两魂人。来自北美原住民文化的术语，“体内同时含有男人和女人灵魂的人”。和两性人Androgyne 基本同义，但和来自希腊文的冷冰冰医学术语不同，这个北美词语强调的是其神秘主义和浪漫主义特性。
    """
    AGENDER = 1
    ANDROGYNE = 2
    ANDROGYNOUS = 3


class User(Base):
    """用户"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    password = Column(String(64))
    email = Column(String(60), unique=True)
    avatar = Column(String(240), nullable=True, doc="用户头像")
    birthday = Column(Date, nullable=True)
    sex = Column(Enum(UserSexEnum), nullable=True)

    def __repr__(self):
        return "<User {}>".format(self.name)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


