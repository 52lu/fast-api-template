from sqlalchemy import Column, Index, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import BIGINT, TINYINT, VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class YmUser(Base):
    __tablename__ = 'ym_user'
    __table_args__ = (
        Index('idx_nick_name', 'nick_name'),
        Index('idx_phone', 'phone'),
        {'comment': '用户表'}
    )

    id = Column(BIGINT, primary_key=True, comment='主键')
    union_id = Column(String(64), nullable=False, server_default=text("''"), comment='微信开放平台下的用户唯一标识')
    open_id = Column(String(64), nullable=False, server_default=text("''"), comment='微信openid')
    nick_name = Column(String(32), nullable=False, server_default=text("''"), comment='昵称')
    password = Column(String(64), nullable=False, server_default=text("''"), comment='密码')
    avatar = Column(String(255), nullable=False, server_default=text("''"), comment='头像')
    phone = Column(String(11), nullable=False, server_default=text("''"), comment='手机号')
    email = Column(String(50), nullable=False, server_default=text("''"), comment='电子邮箱')
    last_login = Column(String(20), nullable=False, server_default=text("''"), comment='上次登录时间')
    status = Column(TINYINT, nullable=False, server_default=text("'1'"), comment='状态；-1:黑名单 1:正常')
    delete_at = Column(String(20), nullable=False, server_default=text("''"), comment='删除时间')
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='创建时间')
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), comment='更新时间')


class YmUserInfo(Base):
    __tablename__ = 'ym_user_info'
    __table_args__ = (
        Index('idx_uid', 'uid'),
        {'comment': '用户信息表'}
    )

    id = Column(BIGINT, primary_key=True, comment='主键')
    uid = Column(BIGINT, nullable=False, server_default=text("'0'"), comment='用户id')
    sex = Column(TINYINT, nullable=False, server_default=text("'-1'"), comment='性别；-1:未知 1:男 2:女 ')
    province = Column(VARCHAR(45), nullable=False, comment='省市')
    city = Column(VARCHAR(45), nullable=False, comment='城市')
    county = Column(VARCHAR(45), nullable=False, comment='区域')
    address = Column(String(255), nullable=False, server_default=text("''"), comment='详细地址')
    delete_at = Column(String(20), nullable=False, server_default=text("''"), comment='删除时间')
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='创建时间')
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), comment='更新时间')
