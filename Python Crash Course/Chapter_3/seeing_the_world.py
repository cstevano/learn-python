places_to_visit = ['Japan', 'Hawaii', 'Korea', 'Maldives', 'America']

print("Original order of list:")
print(places_to_visit)

print("\nTemporarily sorted list using sorted()")
print(sorted(places_to_visit))

print("\nOriginal order of list again:")
print(places_to_visit)

print("\nTemporarily sorted list using sorted(reverse=True)")
print(sorted(places_to_visit, reverse=True))

print("\nOriginal order of list again:")
print(places_to_visit)

print("\nReversing the order by using reverse()")
places_to_visit.reverse()
print(places_to_visit)

print("\nChanging back to original order by using reverse()")
places_to_visit.reverse()
print(places_to_visit)

print("\nSorting the list alphabetically permanent with sort()")
places_to_visit.sort()
print(places_to_visit)

print("\nReverse-sorting the list alphabetically permanent with sort(reverse=True)")
places_to_visit.sort(reverse=True)
print(places_to_visit)