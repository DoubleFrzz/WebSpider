CREATE DATABASE IF NOT EXISTS `webspider`;

CREATE TABLE IF NOT EXISTS `webspider`.`douban` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT, -- （）显示多少位宽
    `name` varchar(64) NOT NULL,
    `rank` int(5) unsigned DEFAULT NULL,
    `moive_link` varchar(256) DEFAULT NULL,
    `img_link` varchar(256) DEFAULT NULL,
    `rate` FLOAT(5, 2) DEFAULT 0,
    `judge_number` bigint(20) unsigned DEFAULT '0',
    `infomation` varchar(128) DEFAULT NULL,
    `created_at` datetime NOT NULL,
    PRIMARY KEY(`id`),
    UNIQUE KEY(`name`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;
