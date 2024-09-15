import 'package:flutter/material.dart';

class MarketHome extends StatelessWidget {
  const MarketHome({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Accueil Marché'),
      ),
      body: Center(
        child: const Text('Bienvenue sur la plateforme Marché.'),
      ),
    );
  }
}
