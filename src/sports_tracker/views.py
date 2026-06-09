from django.shortcuts import render

def home(request):
    """Renders the static welcome page."""
    return render(request, 'sports_tracker/home.html')

def item_list(request):
    """Displays a hardcoded collection of sports items without a database."""
    # We use a standard Python list of dictionaries to simulate database rows
    mock_sports_data = [
        {
            'id': 1, 
            'name': 'UEFA Champions League Final', 
            'sport_type': 'Football', 
            'description': 'Real Madrid vs Borussia Dortmund. Tactical notes: Watch transition speed.',
            'date_added': 'June 07, 2026'
        },
        {
            'id': 2, 
            'name': 'NBA Finals - Game 1', 
            'sport_type': 'Basketball', 
            'description': 'Boston Celtics hosting at TD Garden. Focus on three-point shooting percentages.',
            'date_added': 'June 08, 2026'
        },
        {
            'id': 3, 
            'name': 'Kenya National Athletics Trials', 
            'sport_type': 'Athletics', 
            'description': '10,000m and 1,500m selections for international championships.',
            'date_added': 'June 09, 2026'
        },
        {
            'id': 4, 
            'name': 'WRC Safari Rally Kenya', 
            'sport_type': 'Motorsport', 
            'description': 'World Rally Championship event testing drivers against harsh terrain, deep dust, and unpredictable weather conditions.',
            'date_added': 'June 10, 2026'
        },
        {
            'id': 5, 
            'name': 'Wimbledon Grand Slam', 
            'sport_type': 'Tennis', 
            'description': 'The oldest and most prestigious tennis tournament in the world, played on traditional grass courts.',
            'date_added': 'June 11, 2026'
        },
        {
            'id': 6, 
            'name': 'Kip Keino Classic', 
            'sport_type': 'Athletics', 
            'description': 'An annual international track and field meet featuring elite global sprinters and middle-distance runners.',
            'date_added': 'June 12, 2026'
        },
        {
            'id': 7, 
            'name': 'World Rugby Sevens Series', 
            'sport_type': 'Rugby', 
            'description': 'High-octane, fast-paced international rugby tournament tracking top-tier global teams.',
            'date_added': 'June 13, 2026'
        },
        {
            'id': 8, 
            'name': 'Formula 1 Monaco Grand Prix', 
            'sport_type': 'Motorsport', 
            'description': 'A tight, historic street circuit race requiring absolute precision and making overtaking incredibly challenging.',
            'date_added': 'June 14, 2026'
        },
        {
            'id': 9, 
            'name': 'Local Derby Match', 
            'sport_type': 'Football', 
            'description': 'A heated regional rivalry match. High emotional stakes, intense crowd energy, and tactical physical battles.',
            'date_added': 'June 15, 2026'
        }
    ]
    return render(request, 'sports_tracker/item_list.html', {'items': mock_sports_data})

def item_detail(request, item_id):
    """Finds the single requested item from our static list."""
    # Re-declare the exact same mock list inside the detail view
    mock_sports_data = [
        {'id': 1, 'name': 'UEFA Champions League Final', 'sport_type': 'Football', 'description': 'Real Madrid vs Borussia Dortmund. Tactical notes: Watch transition speed.', 'date_added': 'June 07, 2026'},
        {'id': 2, 'name': 'NBA Finals - Game 1', 'sport_type': 'Basketball', 'description': 'Boston Celtics hosting at TD Garden. Focus on three-point shooting percentages.', 'date_added': 'June 08, 2026'},
        {'id': 3, 'name': 'Kenya National Athletics Trials', 'sport_type': 'Athletics', 'description': '10,000m and 1,500m selections for international championships.', 'date_added': 'June 09, 2026'}
    ]
    
    # Loop through our local list to find the item matching the ID from the URL
    selected_item = None
    for item in mock_sports_data:
        if item['id'] == item_id:
            selected_item = item
            break

    return render(request, 'sports_tracker/item_detail.html', {'item': selected_item})