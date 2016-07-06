#encoding=utf-8
import json

#树的后根遍历
def traverse(node, func):
	if node and node['children']:
		for child in node['children']:
			traverse(child, func)
	func(node)

#清除节点的parent属性，树使用孩子表示法进行表示
def clear_parent(node):
	if node:
		del node['parent']

root = {'code':'','name':'中国','children':[],'parent':None}
cur_node = root
cur_depth = 0
f = open('./xzqh.txt','r')
for line in f:
	code,name = line.split()
	node = {'code':code,'name':name,'children':[],'parent':None}
	node_depth = line.count(' ') / 2 - 1
	if node_depth > cur_depth:
		node['parent'] = cur_node
		cur_node['children'].append(node)
	else :
		while node_depth < cur_depth and cur_node['parent']:
			cur_node = cur_node['parent']
			cur_depth -= 1
		if cur_node['parent']:
			node['parent'] = cur_node['parent']
			cur_node['parent']['children'].append(node)
	cur_node = node
	cur_depth = node_depth

traverse(root, clear_parent)
print json.dumps(root["children"])