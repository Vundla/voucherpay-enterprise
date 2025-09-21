import { Resolver, Query, Arg } from 'type-graphql';

@Resolver()
export class JobResolver {
  @Query(() => String)
  jobs(): string {
    return 'Jobs GraphQL endpoint - Inclusive employment opportunities';
  }

  @Query(() => String)
  accessibleJobs(@Arg('accommodations') accommodations: string): string {
    return `Accessible jobs with accommodations: ${accommodations}`;
  }
}