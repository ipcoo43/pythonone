print('딕셔너리에서 인덱스와 값')

dict_a = { 
	'키A':'값A',
	'키B':'값B',
	'키C':'값C'
}

for index, element in dict_a.items():
	print('{}는 {} 입니다.'.format(index, element))