# Do you really know base

这题题目给了 Base 的关键词，所以我们知道与 Base 编码方式有关

题目提供的 `base.txt` 里面是乱码

`Πଟƨഩ३ୟಇॸҳնŚटиఫஉϱզұઘ൮ପଷචȩӄɘਥවǳஈЙԓӃʜฦഗшʙĪলԴञƌဤɺǍర௦ɣஈયरøɡȈȹʁछƦੴŹʥëϕӳෆไरǲୟপർќɝУӍଜƥ๒ϻϚଋѧඩŨƙĉĔϙଌ৮Ӑɬல৵ñՍҧƚနɳȕ࿓হѣడҍང४ଈϿளɺझถ๑ŲʈཤॠԬҪমపбಊਧঈУո๘၊ǷǭʊЀҴथѷ१ཧ୫ӢϓЋҷটఘèଭӣॸΡəЛ൰ఝșǉЋϼФпঐŹౘƬπզఙએ๐дஃ࿐Ϩ`

结合我们题目的描述

> 为什么我的 Base 是乱码？好像说来自一个小蓝鸟公司？还与 2 的 11 次方有关？最后还可以一把梭？

- 小蓝鸟指的是 Twitter
- 2 的 11 次方是 2048

结合以上信息我们去搜索，关键词：`Twitter` `Base` `2048`，很容易搜到 `Base2048` 这个东西

所以先解一层 Base2048

```python
import base2048

with open("base.txt", "rt", encoding="utf8") as f:
    data = f.read()
    decoded_data = base2048.decode(data)
    print(decoded_data.decode())
```

得到 `B4ptbxqMn4EcOHMAeOijraxLbldJMLsQiefbUhbgSTCzeGsYaUnvCTusPTfwStCmUn4u6wBpphJAy80HsLaryAbEkZ3aBreMcvNYfuI3J29v2jIT1kg1P6BHTI46C3sYYdX2vl8mvSfUzlyZVqzq8sBSuf7PSQlQdr9t3rlF9ZEAredQROSfxrnKNRocpqsCncOZJCOLz2Y0SJZTEBFeEdk0VHJzMjMWEqsmGb0xVRhlEGRzRX`

题目后面还说可以一把梭，我们搜索 `Base` `一把梭` 很容易搜索到一个工具叫做 `basecrack`

> [mufeedvh/basecrack: Decode All Bases - Base Scheme Decoder](https://github.com/mufeedvh/basecrack)

按照这个程序的提示，我们直接一把梭

```shell
$ basecrack -m -b B4ptbxqMn4EcOHMAeOijraxLbldJMLsQiefbUhbgSTCzeGsYaUnvCTusPTfwStCmUn4u6wBpphJAy80HsLaryAbEkZ3aBreMcvNYfuI3J29v2jIT1kg1P6BHTI46C3sYYdX2vl8mvSfUzlyZVqzq8sBSuf7PSQlQdr9t3rlF9ZEAredQROSfxrnKNRocpqsCncOZJCOLz2Y0SJZTEBFeEdk0VHJzMjMWEqsmGb0xVRhlEGRzRX
```

得到 Base 的路径为

`Base62 -> Base64 -> Base58 -> Ascii85 -> Base92 -> Base32`

也同时得到 flag

`flag{Wow_yOU_4r3_THE_bAs3-m@St3r->w<}`