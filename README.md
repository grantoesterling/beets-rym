# Beets RYM Genres Plugin

A [beets](https://beets.io/) plugin that fetches genre, style, mood, and grouping data from Rate Your Music (RYM) scraped data and applies it to your music collection during import.

## Features

- **Automatic Genre Tagging**: Fetches primary genres from RYM during import
- **Secondary Genres**: Applies secondary genres to the `style` field  
- **Descriptors**: Adds mood descriptors to the `mood` field
- **Hierarchical Groupings**: Automatically derives parent genres for the `grouping` field
- **Flexible Matching**: Intelligent fuzzy matching for artist and album names
- **Caching**: Built-in caching to reduce API calls and improve performance
- **Manual Commands**: CLI commands to update existing albums with RYM data
- **FLAC Array Support**: Proper multi-value tag support for FLAC files

## Installation

### Prerequisites

- Python 3.7+
- [beets](https://beets.io/) 1.4.0+

### Install from Source

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/beets-rym-genres.git
   cd beets-rym-genres
   ```

2. Install the plugin:
   ```bash
   pip install -e .
   ```

3. Add the plugin to your beets configuration:
   ```yaml
   plugins: 
     - rym_genres
     # ... your other plugins
   ```

## Configuration

Add the following to your beets `config.yaml`:

```yaml
rym_genres:
    # Required: Firebase URL for RYM data (you must obtain this separately)
    firebase_url: 'YOUR_FIREBASE_URL_HERE'
    
    # Matching thresholds
    similarity_threshold: 0.8          # Minimum similarity for artist/album matching
    title_match_threshold: 0.95        # High title match threshold for flexible matching
    flexible_artist_matching: true     # Allow matches with very high title similarity
    
    # Tag limits
    max_genres: 10                     # Maximum primary genres
    max_styles: 20                     # Maximum secondary genres  
    max_moods: 60                      # Maximum descriptors
    max_groupings: 30                  # Maximum parent genres
    
    # Behavior settings
    auto_tag: true                     # Auto-tag during import
    use_hierarchy: true                # Enable hierarchical parent genre tagging
    require_rym_match: true            # Fail import if no RYM match found
    
    # Caching
    cache_duration: 3600               # Cache duration in seconds (1 hour)
    
    # Logging
    log_missing_matches: true          # Log albums without RYM matches
    missing_matches_logfile: './rym_missing_matches.log'
```

**Important**: You must configure your own Firebase URL that contains Rate Your Music scraped data. The plugin does not include access to any data source by default.

**Note**: The plugin automatically handles data file paths (genre tree, excluded genres, and cache files) - no need to configure these manually.

## Data Source Setup

This plugin requires access to Rate Your Music data in a specific JSON format. You have a few options:

### Option 1: Use Your Own Firebase Database

1. Set up a Firebase Realtime Database
2. Populate it with RYM data in the expected format (see Data Format section below)
3. Configure the `firebase_url` to point to your database's JSON endpoint

### Option 2: Use a Local or Alternative API

The plugin can work with any HTTP endpoint that returns JSON data in the expected format. Simply set the `firebase_url` to your API endpoint.

### Expected Data Format

The plugin expects JSON data in this structure:
```json
{
  "artist_key": {
    "album_key": {
      "artistName": "Artist Name",
      "releaseTitle": "Album Title",
      "genres": ["Genre1", "Genre2"],
      "secondaryGenres": ["SecondaryGenre1"],
      "descriptors": ["descriptor1", "descriptor2"]
    }
  }
}
```

**Note**: This plugin is designed to work with scraped RYM data but does not provide the data itself. Users are responsible for obtaining RYM data through their own means in compliance with Rate Your Music's terms of service.

## Usage

### Automatic Import

Once configured, the plugin will automatically fetch and apply RYM genre data during beets import:

```bash
beet import /path/to/music
```

### Manual Tagging

Update existing albums with RYM genre data:

```bash
# Update all albums
beet rym

# Update specific albums
beet rym artist:"Pink Floyd"
beet rym album:"Dark Side of the Moon"
```

### Tag Mapping

The plugin maps RYM data to the following beets fields:

- **Genres** → `genre` field (primary RYM genres)
- **Secondary Genres** → `style` field (secondary RYM genres)  
- **Descriptors** → `mood` field (RYM descriptors)
- **Groupings** → `grouping` field (hierarchical parent genres)

## Data Files

The plugin includes several data files that are automatically located:

- `rym-genre-tree.json`: Complete RYM genre hierarchy (24,000+ genres)
- `excluded-meta-genres.json`: Meta-genres excluded from tagging (too broad)
- `rym_genres_cache.json`: Local cache for improved performance

### Customizing Data Files

The data files are automatically included with the plugin installation. If you need to customize the excluded genres, you can:

1. Find the plugin's data directory (usually in your Python site-packages)
2. Edit the `excluded-meta-genres.json` file
3. Restart beets to load the changes

## Advanced Features

### Hierarchical Genre Tagging

When `use_hierarchy: true`, the plugin automatically adds parent genres. For example:
- If an album has "Post-Rock" genre
- The plugin will also add "Rock" and "Experimental Rock" as groupings

### Flexible Artist Matching

The plugin includes intelligent matching that handles:
- Artist name variations and aliases
- Articles (The, A, An) in different positions
- Special characters and Unicode normalization
- Multi-artist releases and collaborations

### Caching

Results are cached locally to improve performance:
- Default cache duration: 1 hour
- Cache location: Automatically managed by the plugin
- Automatic cache cleanup and refresh

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [beets](https://beets.io/) - The excellent music library management system
- [Rate Your Music](https://rateyourmusic.com/) - For the comprehensive music genre data
- The beets community for plugin development guidance

## Support

For issues and questions:
- Check the [Issues](https://github.com/yourusername/beets-rym-genres/issues) page
- Review the beets [documentation](https://beets.readthedocs.io/)
- Join the beets [discussion forum](https://github.com/beetbox/beets/discussions) 