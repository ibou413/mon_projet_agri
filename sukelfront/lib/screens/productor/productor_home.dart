import 'package:flutter/material.dart';

class ProductorHome extends StatelessWidget {
  const ProductorHome({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Accueil Producteurs'),
      ),
      body: Center(
        child: const Text('Bienvenue sur la plateforme Producteurs.'),
      ),
    );
  }
}
