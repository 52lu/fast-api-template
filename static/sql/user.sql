-- ym_user definition
CREATE TABLE `ym_user` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `union_id` varchar(64) NOT NULL DEFAULT '' COMMENT '微信开放平台下的用户唯一标识',
  `open_id` varchar(64) NOT NULL DEFAULT '' COMMENT '微信openid',
  `nick_name` varchar(32) NOT NULL DEFAULT '' COMMENT '昵称',
  `password` varchar(64) NOT NULL DEFAULT '' COMMENT '密码',
  `avatar` varchar(255) NOT NULL DEFAULT '' COMMENT '头像',
  `phone` varchar(11) NOT NULL DEFAULT '' COMMENT '手机号',
  `email` varchar(50) NOT NULL DEFAULT '' COMMENT '电子邮箱',
  `last_login` varchar(20) NOT NULL DEFAULT '' COMMENT '上次登录时间',
  `status` tinyint NOT NULL DEFAULT '1' COMMENT '状态；-1:黑名单 1:正常',
  `delete_at` varchar(20) NOT NULL DEFAULT '' COMMENT '删除时间',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `idx_phone` (`phone`) USING BTREE,
  KEY `idx_nick_name` (`nick_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户表';


CREATE TABLE `ym_user_info` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `uid` bigint unsigned NOT NULL DEFAULT '0' COMMENT '用户id',
  `sex` tinyint NOT NULL DEFAULT '-1' COMMENT '性别；-1:未知 1:男 2:女 ',
  `province` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '省市',
  `city` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '城市',
  `county` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '区域',
  `address` varchar(255) NOT NULL DEFAULT '' COMMENT '详细地址',
  `delete_at` varchar(20) NOT NULL DEFAULT '' COMMENT '删除时间',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `idx_uid` (`uid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户信息表';