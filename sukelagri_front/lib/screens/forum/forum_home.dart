import 'package:flutter/material.dart';

class ForumHome extends StatelessWidget {
  const ForumHome({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Accueil Forum'),
      ),
      body: Center(
        child: const Text('Bienvenue sur la plateforme Forum.'),
      ),
    );
  }
}
