def apriori(transactions, support):
    # Calculer le support minimum
    min_support = support * len(transactions)
    
    # Trouver tous les items fréquents de taille 1
    items = {}
    for transaction in transactions:
        for item in transaction:
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
    
    frequent_items = {frozenset([item]): count for item, count in items.items() if count >= min_support}
    
    # La variable L contiendra tous les itemsets fréquents
    L = [frequent_items]

    # La variable k contiendra les itemsets fréquents de taille k
    k = 1
    while len(L[k-1]) > 0:
        # Générer tous les itemsets candidats de taille k+1
        C = set([i.union(j) for i in L[k-1] for j in L[k-1] if len(i.union(j)) == k+1])
        
        # Calculer le nombre d'occurrences de chaque itemset candidat
        itemset_counts = {}
        for transaction in transactions:
            for candidate in C:
                if candidate.issubset(transaction):
                    if candidate in itemset_counts:
                        itemset_counts[candidate] += 1
                    else:
                        itemset_counts[candidate] = 1
        
        # Identifier les itemsets fréquents de taille k+1
        frequent_itemsets = {itemset: count for itemset, count in itemset_counts.items() if count >= min_support}
        
        # Ajouter les itemsets fréquents de taille k+1 à la liste des itemsets fréquents
        L.append(frequent_itemsets)
        
        # Passer à la prochaine taille d'itemset
        k += 1
    
    # Concaténer tous les itemsets fréquents dans une seule liste
    frequent_itemsets = {itemset: count for sublist in L for itemset, count in sublist.items()}
    
    return frequent_itemsets
transactions = [
    frozenset(['bread', 'milk']),
    frozenset(['bread', 'diapers', 'beer', 'eggs']),
    frozenset(['milk', 'diapers', 'beer', 'cola']),
    frozenset(['bread', 'milk', 'diapers', 'beer']),
    frozenset(['bread', 'milk', 'diapers', 'cola'])
]

# Appeler la fonction apriori pour trouver les itemsets fréquents
frequent_itemsets = apriori(transactions, 0.5)

# Afficher les itemsets fréquents
for itemset in frequent_itemsets:
    print(itemset)